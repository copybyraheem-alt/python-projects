class LegacyPrinter:
    def print_document(self, text):
        return f"print document says: {text} "

    def output(self, text):
        return self.print_document(text)

    

class ModernScreen:
    def display(self, content):
        return f"Display says: {content}"
    
    def output(self, content):
        return self.display(content)


class BrailleDisplay:
    def render_dots(self, data):
        return f"Render says: {data}"
        
    def output(self,data):
        return self.render_dots(data)


objs= [LegacyPrinter(), ModernScreen(), BrailleDisplay()]

def send_to_output(device, content):
    print(device.output(content))


for obj in objs:
    send_to_output(obj, "hi")