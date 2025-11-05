import json
import logging
import os
import xml.etree.ElementTree as ET
from typing import Tuple

MARKDOWN_SUFFIX = '.md'


class XmlElementConvert(object):
    """
    XML Element 转换规则
    """

    @staticmethod
    def convert_para_func(**kwargs):
        # 正常文本
        # 粗体、斜体、删除线、链接
        return kwargs.get('text')

    @staticmethod
    def convert_heading_func(**kwargs):
        # 标题
        level = kwargs.get('element').attrib.get('level', 0)
        level = 1 if level in (['a', 'b']) else level
        text = kwargs.get('text')
        return ' '.join(["#" * int(level), text]) if text else text

    @staticmethod
    def convert_image_func(**kwargs):
        # 图片
        image_url = XmlElementConvert.get_text_by_key(list(kwargs.get('element')), 'source')
        return '![{text}]({image_url})'.format(text=kwargs.get('text'), image_url=image_url)

    @staticmethod
    def convert_attach_func(**kwargs):
        # 附件
        element = kwargs.get('element')
        filename = XmlElementConvert.get_text_by_key(list(element), 'filename')
        resource_url = XmlElementConvert.get_text_by_key(list(element), 'resource')
        return '[{text}]({resource_url})'.format(text=filename, resource_url=resource_url)

    @staticmethod
    def convert_code_func(**kwargs):
        # 代码块
        language = XmlElementConvert.get_text_by_key(list(kwargs.get('element')), 'language')
        return '```{language}\r\n{code}```'.format(language=language, code=kwargs.get('text'))

    @staticmethod
    def convert_todo_func(**kwargs):
        # to-do
        return '- [ ] {text}'.format(text=kwargs.get('text'))

    @staticmethod
    def convert_quote_func(**kwargs):
        # 引用
        return '> {text}'.format(text=kwargs.get('text'))

    @staticmethod
    def convert_horizontal_line_func(**kwargs):
        # 分割线
        return '---'

    @staticmethod
    def convert_list_item_func(**kwargs):
        # 列表
        list_id = kwargs.get('element').attrib['list-id']
        is_ordered = kwargs.get('list_item').get(list_id)
        text = kwargs.get('text')
        if is_ordered == 'unordered':
            return '- {text}'.format(text=text)
        elif is_ordered == 'ordered':
            return '1. {text}'.format(text=text)

    @staticmethod
    def convert_table_func(**kwargs):
        """
        表格转换
        :param kwargs:
        :return:
        """
        element = kwargs.get('element')
        content = XmlElementConvert.get_text_by_key(element, 'content')

        table_data_str = f''  # f-string 多行字符串
        nl = '\r\n'  # 考虑 Windows 系统，换行符设为 \r\n
        table_data = json.loads(content)
        table_data_len = len(table_data['widths'])
        table_data_arr = []
        table_data_line = []

        for cells in table_data['cells']:
            if cells.get('value'):
                cell_value = XmlElementConvert._encode_string_to_md(cells.get('value'))
                table_data_line.append(cell_value)
                # 攒齐一行放到 table_data_arr 中，并重置 table_data_line
                if len(table_data_line) == table_data_len:
                    table_data_arr.append(table_data_line)
                    table_data_line = []

        # 如果只有一行，那就给他加一个空白 title 行
        if len(table_data_arr) == 1:
            table_data_arr.insert(0, [ch for ch in (" " * table_data_len)])
            table_data_arr.insert(1, [ch for ch in ("-" * table_data_len)])
        elif len(table_data_arr) > 1:
            table_data_arr.insert(1, [ch for ch in ("-" * table_data_len)])

        for table_line in table_data_arr:
            table_data_str += "|"
            for table_data in table_line:
                table_data_str += f' %s |' % table_data
            table_data_str += f'{nl}'

        return table_data_str

    @staticmethod
    def get_text_by_key(element_children, key='text'):
        """
        获取文本内容
        :return:
        """
        for sub_element in element_children:
            if key in sub_element.tag:
                return sub_element.text if sub_element.text else ''
        return ''

    @staticmethod
    def _encode_string_to_md(original_text):
        """ 将字符串转义 防止 markdown 识别错误 """

        if len(original_text) <= 0 or original_text == " ":
            return original_text

        original_text = original_text.replace('\\', '\\\\')  # \\ 反斜杠
        original_text = original_text.replace('*', '\\*')  # \* 星号
        original_text = original_text.replace('_', '\\_')  # \_ 下划线
        original_text = original_text.replace('#', '\\#')  # \# 井号

        # markdown 中需要转义的字符
        original_text = original_text.replace('&', '&amp;')
        original_text = original_text.replace('<', '&lt;')
        original_text = original_text.replace('>', '&gt;')
        original_text = original_text.replace('“', '&quot;')
        original_text = original_text.replace('‘', '&apos;')

        original_text = original_text.replace('\t', '&emsp;')

        # 换行 <br>
        original_text = original_text.replace('\r\n', '<br>')
        original_text = original_text.replace('\n\r', '<br>')
        original_text = original_text.replace('\r', '<br>')
        original_text = original_text.replace('\n', '<br>')

        return original_text


class jsonConvert(object):
    """
    json 转换规则
    """
    
    def get_seven_text(self, seven_contents: list,is_add_attr: bool=True) -> str:
        """键7是一个列表,遍历键7获取文本和添加属性,返回带属性的文本

        Args:
            seven_contents (list): 内容
            is_add_attr (bool, optional): 文本是否添加属性. Defaults to True.

        Returns:
            Tuple[list, str]: 文本内容
        """
        
        text = ''
        for seven_content in seven_contents:
            split_text = seven_content.get('8')
            split_text_attrs = seven_content.get('9')
            if split_text and split_text_attrs and is_add_attr:
                split_text = self.convert_text_attribute(split_text, split_text_attrs)
            text += split_text
        return text
    
    def get_five_text(self, five_contents: list,is_add_attr: bool=True) -> str:
        """键5是一个列表,遍历键5获取文本和添加属性,返回带属性的文本

        Args:
            five_contents (list): 内容
            is_add_attr (bool, optional): 文本是否添加属性. Defaults to True.

        Returns:
            Tuple[list, str]: 文本内容
        """
        
        text_list = []
        if five_contents:
            for index,five_content in enumerate(five_contents):
                seven_contents = five_content.get('7')
                next_five_contents =  five_content.get('5')
                # 键7类型
                if seven_contents:
                    split_text = self.get_seven_text(seven_contents=seven_contents, is_add_attr=is_add_attr)
                    text_list.append(split_text)
                    if index == len(five_contents) - 1:
                        return ''.join(text_list)
                # 键5类型
                elif next_five_contents:
                    one_line_text = self.get_five_text(next_five_contents, is_add_attr)
                    text_list.append(one_line_text)
                    if index == len(five_contents) - 1:
                        return ''.join(text_list)
                # 其他类型返回空
                else:
                    return ''
        else:
            return ''

    
    def convert_text_func(self, content: dict, is_add_attr: bool=True) -> str:
        """ 正常文本 """
        text_list=[]
        five_contents = content.get('5')
        if five_contents:
            for index,five_content in enumerate(five_contents):
                # 下个键5
                next_five_contents: list =  five_content.get('5')
                # 键6类型
                six_type = five_content.get('6')
                # 文本和属性
                seven_contents = five_content.get('7')
                
                # 键6类型
                if six_type:
                    # 已知类型为li,tc
                    convert_func = getattr(self,f'convert_{six_type}_func', None)
                    if convert_func:
                        split_text = convert_func(five_content)
                    else:
                        split_text = self.convert_text_func(five_content)
                        
                    text_list.append(split_text)
                    if index == len(five_contents) - 1:
                       return self.optimize_text(''.join(text_list))
                # 键7类型
                elif seven_contents:
                    split_text = self.get_seven_text(seven_contents=seven_contents, is_add_attr=is_add_attr)
                    text_list.append(split_text)
                    if index == len(five_contents) - 1:
                        return self.optimize_text(''.join(text_list))
                # 键5类型
                elif next_five_contents:
                    one_line_text = self.get_five_text(next_five_contents, is_add_attr)
                    text_list.append(one_line_text)
                    if index == len(five_contents) - 1:
                        return self.optimize_text(''.join(text_list))
                else:
                    return ""
        else:                      
            return ""
    
    
    def convert_li_func(self,content: dict):
        """链接

        Args:
            content (dict): 类型为li的字典

        Returns:
            _type_: 返回链接
        """
        text = ""
        # 为兼容obsidian，链接类型不添加属性
        source_text = self.convert_text_func(content,is_add_attr=False)
        # 附加信息
        four_content: dict = content.get('4')
        if four_content:
            hf = four_content.get('hf')
            text = f'[{source_text}]({hf})'
        return text

    def convert_text_attribute(self, text: str, text_attrs: list):
        """文本属性, 粗体、斜体、删除线、链接、颜色、下划线"""
        if isinstance(text_attrs, list) and text_attrs and text:
            for attr in text_attrs:
                if attr['2'] == "b":
                    # 粗体
                    text = f"**{text}**"
                elif attr['2'] == "i":
                    # 斜体
                    text = f"*{text}*"
                elif attr['2'] == "u":
                    # 下划线
                    text = f"<u>{text}</u>"
                elif attr['2'] == "c":
                    # 颜色
                    text = f'<font color= "{attr["0"]}">{text}</font>'
        return text

    def convert_h_func(self, content: dict) -> str:
        """标题

        Args:
            content (dict): 类型为h的字典

        Returns:
            str: _description_
        """
        type_name = content.get('4').get('l')
        text = self.convert_text_func(content=content)
        if text and type_name:
            level_str = type_name.replace('h', '')
            level = int(level_str)
            text = ' '.join(["#" * int(level), text])
        return text

    def convert_im_func(self, content):
        # 图片
        image_url = content["4"]["u"]
        return '![]({image_url})'.format(image_url=image_url)

    def convert_a_func(self, content):
        # 附件
        fn = content["4"]["fn"]
        fl = content["4"]["re"]
        return '[{text}]({resource_url})'.format(text=fn, resource_url=fl)

    def convert_cd_func(self, content):
        # 代码块
        language = content.get('4').get('la')
        codes: list = content.get('5')
        code_block = ""
        for code in codes:
            text = self.convert_text_func(code)
            if text:
                code_block += text + '\n'

        return '```{language}\r\n{code_block}```'.format(language=language, code_block=code_block)

    def convert_q_func(self, content):
        """引用"""
        q_text_list = content['5']
        text = ''
        for q_text_dict in q_text_list:
            q_text = self.convert_text_func(q_text_dict)
            # 去除第一行的换行
            q_text = q_text.replace('\n', '')
            text += "> {q_text}\n".format(q_text=q_text)
        return text

    def convert_l_func(self, content):
        """有序列表和无序列表,有序列表转成无序列表"""
        text = self.convert_text_func(content=content)
        is_ordered = content.get('4').get('lt')   # unordered or ordered
        if is_ordered == 'ordered':
            # 有序列表都设置为1,有些md编辑自动转为有序列表
            return f'1. {text}'
        else:
            return f'- {text}'
    
    def convert_tc_func(self, content: dict) -> str:
        """表格的列

        Args:
            content (dict): 键6类型为"tc"字典

        Returns:
            str: 单元格文本
        """
        five_content_list: list = content.get('5')
        table_cell_list = []
        table_cell_text = ""
        for item_content in five_content_list:
            one_line_text = self.convert_text_func(item_content)
            table_cell_list.append(one_line_text)
        table_cell_text =  '<br />'.join(table_cell_list)
        return table_cell_text

    def convert_t_func(self, content: dict) -> str:
        """表格 

        Args:
            content (dict): 键6类型为"t"字典

        Returns:
            str: 整个表格内容
        """

        nl = '\r\n'  # 考虑 Windows 系统，换行符设为 \r\n
        # 行列表
        table_row_list = content['5']  
        table_lines = '\r\n'

        for index, table_row in enumerate(table_row_list):
            # 列的列表
            table_column_list = table_row['5']
            # 列的数量
            table_content_len = len(table_column_list)
            
            if index == 1:
                table_line = '| -- ' * table_content_len + '|\n| '
            else:
                table_line = '| '
                
            for table_column in table_column_list:
                table_text = self.convert_tc_func(table_column)
                table_line = table_line + table_text + ' | '
            table_lines = table_lines + table_line + f'{nl}'
        return table_lines

    def convert_hr_func(self, content: dict) -> str:
        """分割线
        """
        return '---'

    def convert_la_func(self, content: dict) -> str:
        """
        高亮文本, 按之前逻辑加<mark>标记
        """
        la_text_list = content['5']
        text = ''
        for q_text_dict in la_text_list:
            q_text = self.convert_text_func(q_text_dict)
            q_text = q_text.replace('\n', '')
            text += f"<mark>{q_text}</mark>"
        return text

    def convert_drawio_ynote_func(self, content: dict) -> str:
        return self.convert_im_func(content=content)

    def convert_excalidraw_func(self, content: dict) -> str:
        return self.convert_im_func(content=content)

    def convert_mindmap_func(self, content: dict) -> str:
        return self.convert_im_func(content=content)

    def convert_media_func(self, content: dict) -> str:
        sr = content.get("4", {}).get("sr", "outside link:")
        hf = content.get("4", {}).get("hf", "")
        return f'[{sr}]({hf})'

    def _encode_string_to_md(self, original_text):
        """ 将字符串转义 防止 markdown 识别错误 """

        if len(original_text) <= 0 or original_text == " ":
            return original_text

        original_text = original_text.replace('\\', '\\\\')  # \\ 反斜杠
        original_text = original_text.replace('*', '\\*')  # \* 星号
        original_text = original_text.replace('_', '\\_')  # \_ 下划线
        original_text = original_text.replace('#', '\\#')  # \# 井号

        # markdown 中需要转义的字符
        original_text = original_text.replace('&', '&amp;')
        original_text = original_text.replace('<', '&lt;')
        original_text = original_text.replace('>', '&gt;')
        original_text = original_text.replace('“', '&quot;')
        original_text = original_text.replace('‘', '&apos;')

        original_text = original_text.replace('\t', '&emsp;')

        # 换行 <br>
        original_text = original_text.replace('\r\n', '<br>')
        original_text = original_text.replace('\n\r', '<br>')
        original_text = original_text.replace('\r', '<br>')
        original_text = original_text.replace('\n', '<br>')

        return original_text
    
    @classmethod
    def optimize_text(cls,text: str):
        text = text.strip('\r')
        return text
        


class YoudaoNoteConvert(object):
    """
    有道云笔记 xml或者json 内容转换为 markdown 内容
    """

    @staticmethod
    def covert_html_to_markdown(file_path) -> str:
        """
        转换 HTML 为 MarkDown
        :param file_path:
        :return:
        """
        with open(file_path, 'rb') as f:
            content_str = f.read().decode('utf-8')
        from markdownify import markdownify as md
        # 如果换行符丢失，使用 md(content_str.replace('<br>', '<br><br>').replace('</div>', '</div><br><br>')).rstrip()
        new_content = md(content_str)
        base = os.path.splitext(file_path)[0]
        new_file_path = ''.join([base, MARKDOWN_SUFFIX])
        os.rename(file_path, new_file_path)
        with open(new_file_path, 'wb') as f:
            f.write(new_content.encode())
        return new_file_path

    @staticmethod
    def covert_xml_to_markdown_content(file_path):
        # 使用 xml.etree.ElementTree 将 xml 文件转换为对象
        element_tree = ET.parse(file_path)
        note_element = element_tree.getroot()  # note Element

        # list_item 的 id 与 type 的对应
        list_item = {}
        for child in note_element[0]:
            if 'list' in child.tag:
                list_item[child.attrib['id']] = child.attrib['type']

        body_element = note_element[1]  # Element
        new_content_list = []
        for element in list(body_element):
            text = XmlElementConvert.get_text_by_key(list(element))
            name = element.tag.replace('{http://note.youdao.com}', '').replace('-', '_')
            convert_func = getattr(XmlElementConvert, 'convert_{}_func'.format(name), None)
            # 如果没有转换，只保留文字
            if not convert_func:
                new_content_list.append(text)
                continue
            line_content = convert_func(text=text, element=element, list_item=list_item)
            new_content_list.append(line_content)
        return f'\r\n\r\n'.join(new_content_list)  # 换行 1 行

    @staticmethod
    def covert_xml_to_markdown(file_path) -> str:
        """
        转换 XML 为 MarkDown
        :param file_path:
        :return:
        """
        base = os.path.splitext(file_path)[0]
        new_file_path = ''.join([base, MARKDOWN_SUFFIX])
        # 如果文件为空，结束
        if os.path.getsize(file_path) == 0:
            os.rename(file_path, new_file_path)
            return None

        new_content = YoudaoNoteConvert.covert_xml_to_markdown_content(file_path)
        with open(new_file_path, 'wb') as f:
            f.write(new_content.encode('utf-8'))
        # 删除旧文件
        if os.path.exists(file_path) and file_path != new_file_path:
            os.remove(file_path)
        return new_file_path

    @staticmethod
    def covert_json_to_markdown_content(file_path):
        all_text=""
        new_content_list = []
        # 加载json文件
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                json_data = json.load(f)
            except Exception as e:
                logging.error(e)
                json_data = {}

        json_contents = json_data['5']
        for content in json_contents:
            type = content.get('6')
            # 根据类型处理，无类型的为普通文本
            if type:
                clean_type = type.replace('-', '_')
                convert_func = getattr(jsonConvert(), f'convert_{clean_type}_func', None)
                if not convert_func:
                    line_content = jsonConvert().convert_text_func(content)
                else:
                    line_content = convert_func(content)
            else:
                line_content = jsonConvert().convert_text_func(content)
                
            new_content_list.append(str(line_content))
            
        return f'\r\n'.join(new_content_list)  # 换行 1 行

    @staticmethod
    def covert_json_to_markdown(file_path, is_delete: bool=True) -> str:
        """转换 Json 为 MarkDown

        Args:
            file_path (_type_): 文件路径
            is_delete (bool, optional): 是否删除转换前的旧文件. Defaults to True.

        Returns:
            str: 转换后的文件路径
        """

        base = os.path.splitext(file_path)[0]
        new_file_path = ''.join([base, MARKDOWN_SUFFIX])
        # 如果文件为空，结束
        if os.path.getsize(file_path) == 0:
            os.rename(file_path, new_file_path)
            return False
        new_content = YoudaoNoteConvert.covert_json_to_markdown_content(file_path)
        with open(new_file_path, 'wb') as f:
            f.write(new_content.encode('utf-8'))
        # 删除旧文件
        if is_delete:
            if os.path.exists(file_path) and file_path != new_file_path:
                os.remove(file_path)
        return new_file_path

    @staticmethod
    def markdown_filter(file_path):
        filter_list = ['&#x20;']
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        for filter_text in filter_list:
            new_content = content.replace(filter_text, '')

        with open(file_path, 'wb') as f:
            f.write(new_content.encode('utf-8'))


if __name__ == '__main__':
    path = "../test/test.json"
    YoudaoNoteConvert.covert_json_to_markdown(path,False)
