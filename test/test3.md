官方文档：[https://docs.ansible.com/ansible/latest/api/index.html#classes](https://docs.ansible.com/ansible/latest/api/index.html#classes)

案列：[https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html](https://docs.ansible.com/ansible/latest/dev_guide/developing_api.html)

tip:pip3 install ansible的方式安装，ansible.cfg文件会在site-packages/ansible/galaxy/data/container/tests下。

### ansible api官方例子

```
#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json
import shutil
import ansible.constants as C
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.module_utils.common.collections import ImmutableDict
from ansible.inventory.manager import InventoryManager
from ansible.parsing.dataloader import DataLoader
from ansible.playbook.play import Play
from ansible.plugins.callback import CallbackBase
from ansible.vars.manager import VariableManager
from ansible import context
# Create a callback plugin so we can capture the output
class ResultsCollectorJSONCallback(CallbackBase):
    """A sample callback plugin used for performing an action as results come in.
    If you want to collect all results into a single object for processing at
    the end of the execution, look into utilizing the ``json`` callback plugin
    or writing your own custom callback plugin.
    """
    def __init__(self, *args, **kwargs):
        super(ResultsCollectorJSONCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
    def v2_runner_on_unreachable(self, result):
        host = result._host
        self.host_unreachable[host.get_name()] = result
    def v2_runner_on_ok(self, result, *args, **kwargs):
        """Print a json representation of the result.
        Also, store the result in an instance attribute for retrieval later
        """
        host = result._host
        self.host_ok[host.get_name()] = result
        print(json.dumps({host.name: result._result}, indent=4))
    def v2_runner_on_failed(self, result, *args, **kwargs):
        host = result._host
        self.host_failed[host.get_name()] = result
def main():
    host_list = ['192.168.15.124']
    # since the API is constructed for CLI it expects certain options to always be set in the context object
    context.CLIARGS = ImmutableDict(connection='smart', module_path=['/usr/share/ansible/plugins/modules', '/root/venv/bin/ansible'], forks=10, become=None,
                                    become_method=None, become_user=None, check=False, diff=False, verbosity=0)
    # required for
    # https://github.com/ansible/ansible/blob/devel/lib/ansible/inventory/manager.py#L204
    sources = ','.join(host_list)
    if len(host_list) == 1:
        sources += ','
    # initialize needed objects
    loader = DataLoader()  # Takes care of finding and reading yaml, json and ini files
    passwords = dict(vault_pass='!szzsmw123')
    # Instantiate our ResultsCollectorJSONCallback for handling results as they come in. Ansible expects this to be one of its main display outlets
    results_callback = ResultsCollectorJSONCallback()
    
    # sources="/etc/ansible/hosts"
    # create inventory, use path to host config file as source or hosts in a comma separated string
    inventory = InventoryManager(loader=loader, sources=sources)
    # variable manager takes care of merging all the different sources to give you a unified view of variables available in each context
    variable_manager = VariableManager(loader=loader, inventory=inventory)
    # print(variable_manager.get_vars())
    # instantiate task queue manager, which takes care of forking and setting up all objects to iterate over host list and tasks
    # IMPORTANT: This also adds library dirs paths to the module loader
    # IMPORTANT: and so it must be initialized before calling `Play.load()`.
    tqm = TaskQueueManager(
        inventory=inventory,
        variable_manager=variable_manager,
        loader=loader,
        passwords=passwords,
        stdout_callback=results_callback,  # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
    )
    # create data structure that represents our play, including tasks, this is basically what our YAML loader does internally.
    play_source = dict(
        name="Ansible Play",
        hosts=host_list,
        gather_facts='no',
        tasks=[
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
            dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}'))),
            dict(action=dict(module='command', args=dict(cmd='/usr/bin/uptime'))),
        ]
    )
    # Create play object, playbook objects use .load instead of init or new methods,
    # this will also automatically create the task objects from the info provided in play_source
    play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
    # Actually run it
    try:
        result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
    finally:
        # we always need to cleanup child procs and the structures we use to communicate with them
        tqm.cleanup()
        if loader:
            loader.cleanup_all_tmp_files()
    # Remove ansible tmpdir
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
    print("UP ***********")
    for host, result in results_callback.host_ok.items():
        print('{0} >>> {1}'.format(host, result._result['stdout']))
    print("FAILED *******")
    for host, result in results_callback.host_failed.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))
    print("DOWN *********")
    for host, result in results_callback.host_unreachable.items():
        print('{0} >>> {1}'.format(host, result._result['msg']))
if __name__ == '__main__':
    main()
```

### **TaskQueueManager**

TaskQueueManager 字段说明

inventory --> 由ansible.inventory模块创建，用于导入inventory文件

variable_manager --> 由ansible.vars模块创建，用于存储各类变量信息

loader --> 由ansible.parsing.dataloader模块创建，用于数据解析

options --> 存放各类配置信息的数据字典

passwords --> 登录密码，可设置加密信息

stdout_callback --> 回调函数

TaskQueueManager.run方法的返回状态码

```
RUN_OK                = 0    
RUN_ERROR             = 1  
RUN_FAILED_HOSTS      = 2
RUN_UNREACHABLE_HOSTS = 4
RUN_FAILED_BREAK_PLAY = 8
RUN_UNKNOWN_ERROR     = 255
```

### ansible_python_interpreter

组变量ansible_python_interpreter是ansible自带的影藏变量,是facts套件提供的;如果目标机器上python版本多,指定一个版本来运行

如果目标机器上python版本多的话，会警告报错，可能执行不了ansible api

```
[WARNING]: Unhandled error in Python interpreter discovery for host 192.168.15.125: Expecting value: line 1 column 1 (char 0)
```

你可以选择在当前[Python环境](https://so.csdn.net/so/search?q=Python%E7%8E%AF%E5%A2%83&spm=1001.2101.3001.7020)安装python依赖包解决问题，注意：这里的安装包是需要安装在被控制服务器（目标服务器）上的 ； 当然如果系统安装了python3也可以选择python3解释器

运行命令时添加

```
ansible localhost -m ping -e 'ansible_python_interpreter=/usr/bin/python3'
ansible-playbook sample-playbook.yml -e 'ansible_python_interpreter=/usr/bin/python3'
```

添加在ansible.cfg 中

```
localhost-py3 ansible_host=localhost ansible_connection=local ansible_python_interpreter=/usr/bin/python3
k8s-master1 ansible_host=192.100.30.164 ansible_ssh_pass=youpassword
```

添加在ansible-playbook剧本中在tasks中声明

```
- hosts: test_server
  tasks:
    - name: install pip
      apt:
        name: python-pip
      vars:
        ansible_python_interpreter: /usr/bin/python
```

在剧本的范围内

```
- hosts: test_server
  vars:
    ansible_python_interpreter: /usr/bin/python
  tasks:
    - name: install pip
      apt:
        name: python-pip
```