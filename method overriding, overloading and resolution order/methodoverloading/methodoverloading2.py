class StringFormatter:
    def format_text(self, text, style="normal", color=None):
        if style == "normal" and color is None:
            return text
        elif style == "upper" and color is None:
            return text.upper()
        elif style == "normal" and color:
            return f"[{color}]{text}[/{color}]"
        elif style == "upper" and color:
            return f"[{color}]{text.upper()}[/{color}]"
        else:
            return text

formatter = StringFormatter()
print(f"Normal: {formatter.format_text('hello world')}")
print(f"Upper: {formatter.format_text('hello world', 'upper')}")
print(f"With color: {formatter.format_text('hello world', color='red')}")
print(f"Upper + color: {formatter.format_text('hello world', 'upper', 'blue')}")