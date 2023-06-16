class Ex(BaseException):
    def __init__(self, msg) -> None:
        Exception.__init__(self,msg+msg)
        self.args = (msg,)#Si comentamos esta línea el valor de args es ('exex',)

try:
    raise Ex('ex')
except Ex as e:
    print(e)
except Exception as e:
    print(e)
