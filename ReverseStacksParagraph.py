def reverse_paragraph(paragraph):
    words = paragraph.split()  # Split the paragraph into words
    stack = []

    # Push each word onto the stack
    for word in words:
        stack.append(word)

    reversed_paragraph = ""

    # Pop each word off the stack to construct the reversed paragraph
    while stack:
        reversed_paragraph += stack.pop() + " "

    return reversed_paragraph.strip()  # Remove trailing space

def main():
    line = ("--------------------------------------------")

    print(line)
    paragraph = input("Enter a paragraph to reverse: ")
    reversed_paragraph = reverse_paragraph(paragraph)

    print(f"Reversed paragraph: {reversed_paragraph}")
    print(line)

if __name__ == "__main__":
    main()
