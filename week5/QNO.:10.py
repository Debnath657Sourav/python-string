def simple_text_editor(operations):
    text = ""
    history = []
    output = []

    for op in operations:
        if op[0] == "1":  # append
            history.append(text)
            text += op[1]
        elif op[0] == "2":  # delete
            history.append(text)
            k = int(op[1])
            text = text[:-k]
        elif op[0] == "3":  # print
            k = int(op[1])
            output.append(text[k - 1])
        elif op[0] == "4":  # undo
            text = history.pop()

    return output
