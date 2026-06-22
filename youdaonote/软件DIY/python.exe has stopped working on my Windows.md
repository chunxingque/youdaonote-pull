"python.exe has stopped working" on my Windows  
  
QObject::startTimer: Timers can only be used with threads started with QThread  
很危险啊，搞不好会造成程序关闭的时候崩溃  
  
In the QObject.\_\_init\_\_(self, Parent=None) documentation it states:  
The parent argument, if not None, causes self to be owned by Qt instead of PyQt.  
  
If self delete, All child will follow delete   
  
The destructor of a parent object destroys all child objects.Setting parent to 0 constructs an object with no parent. If the object is a widget, it will become a top-level window.  
  
Both of these issues are caused by python deleting objects in an unpredicable order when it exits.  
  
 self.setAttribute(QtCore.Qt.WA\_DeleteOnClose)  
  
 However, for this to be completely successful, all the relevant objects must be linked together in a parent-child hierarchy.   
  
 Qproceess(self)  
 self.downloadtask  
  
  
 Perhaps I should have said "potential oversight" rather than "bug". AFAIUI, Python does not guarantee that objects will be deleted in a specific order when it exits. On the other hand, when Qt deletes an object, it always tries to delete all its children as well, which will normally ensure that objects get deleted in the right order. This is especially important when Qt takes ownership of an object, because you could end up in a situation where an attempt is made to delete the object twice (which will result in a crash).  
  
 exit crashes  
  
 the problem sometimes happens when Python's garbage collection deletes items in the wrong order.  
 gc  
  
 event.ignore()  
  
  
  
 it is a good idea to give QObject instances a parent.  
  
- It's a top level window.- You know it'll be reparented by Qt, e.g. a widget which will be  added to a layout.  
