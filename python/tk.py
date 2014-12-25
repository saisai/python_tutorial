# -*- coding:utf-8 -*-
# Python内置的Tkinter可以满足基本的GUI程序的要求，如果是非常复杂的GUI程序
# 建议用操作系统原生支持的语言和库来编写。

from Tkinter import *
import tkMessageBox

# 在GUI中，每个Button、Label、输入框等，都是一个Widget。
# Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树。

pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameInput = Entry(self)
		self.nameInput.pack()
		self.alertButton = Button(self, text='Hello', command=self.hello)
		self.alertButton.pack()

	def hello(self):
		name = self.nameInput.get() or 'world'
		tkMessageBox.showinfo('Message', 'Hello, %s' % name)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
app.mainloop()