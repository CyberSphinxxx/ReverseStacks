def reverse_paragraph(paragraph):
    stack = []
    reversed_paragraph = ""

    for char in paragraph:
        stack.append(char)

    while stack:
        reversed_paragraph += stack.pop()

    return reversed_paragraph

def main():
    line = ("--------------------------------------------")

    print(line)
    paragraph = input("Enter a paragraph to reverse: ")
    reversed_paragraph = reverse_paragraph(paragraph)

    print(f"Reversed paragraph: {reversed_paragraph}")
    print(line)

if __name__ == "__main__":
    main()
