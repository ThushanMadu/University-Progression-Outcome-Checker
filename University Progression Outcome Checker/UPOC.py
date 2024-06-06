# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20230159/ w2053174
# Date: 14/12/2023

from graphics import *
#create variables
progress=0
trailer=0
retriever=0
exclude=0
total=0
additional_text="Histogram Results"
#create lists
progress_list = []
trailer_list = []
retriever_list = []
exclude_list = []

#validation
print("Part 1:")
def get_pass_mark():
  while True:
    try:
      pass_mark = int(input("\nPlease enter your credits at pass: "))
      if 0 <= pass_mark <= 120 and pass_mark % 20 == 0:
        return pass_mark
      else:
        print("Out of range.")
    except ValueError:
      print("Integer required")

def get_defer_mark():
  while True:
    try:
      defer_mark = int(input("Please enter your credit at defer: "))
      if 0 <= defer_mark <= 120 and defer_mark % 20 == 0:
        return defer_mark
      else:
        print("Out of range.")
    except ValueError:
      print("Integer required.")

def get_fail_mark():
  while True:
    try:
      fail_mark = int(input("Please enter your credit at fail: "))
      if 0 <= fail_mark <= 120 and fail_mark % 20 == 0:
        return fail_mark
      else:
        print("Out of range.")
    except ValueError:
      print("Integer required")


while True:
  # Get pass, defer, and fail marks
  pass_mark = get_pass_mark()
  defer_mark = get_defer_mark()
  fail_mark = get_fail_mark()

  # Calculate total mark
  total_mark = pass_mark + defer_mark + fail_mark

  # Validate total mark
  if total_mark != 120:
    print("Total incorrect.")
    continue

  if pass_mark == 120:
    progression_outcome = "Progress"
    progress += 1
    progress_list.append(f"{pass_mark}, {defer_mark}, {fail_mark}")
  elif pass_mark == 100:
    progression_outcome = "Progress (module trailer)"
    trailer += 1
    trailer_list.append(f"{pass_mark}, {defer_mark}, {fail_mark}")
  elif fail_mark >= 80:
    progression_outcome = "Exclude"
    exclude += 1
    exclude_list.append(f" {pass_mark}, {defer_mark}, {fail_mark}")
  else:
    progression_outcome = "Do not progress - module retriever"
    retriever += 1
    retriever_list.append(f" {pass_mark}, {defer_mark}, {fail_mark}")

  # Print progression outcome
  print(f"{progression_outcome}")

  # Multiple outcome
  while True:
    choice = input("\nWould you like to enter another set of data ? \nEnter 'y' for yes or 'q' to quit and view results: ").lower()
    if choice in ("y", "q"):
      break
    else:
      print("Please enter 'y' or 'q'.")

  if choice == "y":
    continue
  else:
    break

# Part 2: List extension
print("\n..............................................................................................................................")
print("\nPart 2:")
for i in progress_list:
    print("Progress -", i)
for i in trailer_list:
    print("Progress (module trailer) -", i)
for i in retriever_list:
    print("Module retriever -", i)
for i in exclude_list:
    print("Exclude -", i)

# Part 3: File handling
print("\n..............................................................................................................................")
print("\nPart3:")
text = open("Progression file.txt", "w")
text.close()
for i in range(len(progress_list)):
    print("Progress -", *progress_list[i])
    with open("Progression file.txt", "a") as text:
        content = f"Progress - {progress_list[i]}\n"
        text.write(content)
        text.close()
for i in range(len(trailer_list)):
    print("Progress (module trailer) -", *trailer_list[i])
    with open("Progression file.txt", "a") as text:
        content = f"Progress (module trailer) - {trailer_list[i]}\n"
        text.write(content)
        text.close()
for i in range(len(retriever_list)):
    print("module retriever -", *retriever_list[i])
    with open("Progression file.txt", "a") as text:
        content = f"module retriever - {retriever_list[i]}\n"
        text.write(content)
        text.close()
for i in range(len(exclude_list)):
    print("Exclude -", *exclude_list[i])
    with open("Progression file.txt", "a") as text:
        content = f"Exclude - {exclude_list[i]}\n"
        text.write(content)
        text.close()
# Histogram
def draw_text(win, content, size, color, x, y):
    text = Text(Point(x, y), content)
    text.setSize(size)
    text.setTextColor(color)
    text.draw(win)
def draw_bar(win, label, height, color, outline_color, x, y):
    # Create the filled bar
    bar = Rectangle(Point(x, y), Point(x + 50, y - height * 20))
    bar.setFill(color)
    bar.setOutline(outline_color)
    bar.draw(win)
    # Create and draw the text
    text = Text(Point(x + 25, y + 20), f"{label}")
    text.setTextColor("#336699")
    text.draw(win)
def render_graph(progress, trailer, retriever, exclude, total, additional_text):
    win = GraphWin("Histogram", 600, 600)
    win.setBackground("mint cream")

    draw_bar(win, "Progress", progress, "#aef8a1", "#6e7f91", 100, 500)
    draw_bar(win, "Trailer", trailer, "#a0c689", "#6e7f91", 200, 500)
    draw_bar(win, "Retriever", retriever, "#a7bc77", "#6e7f91", 300, 500)
    draw_bar(win, "Exclude", exclude, "#d2b6b5", "#6e7f91", 400, 500)

    # Add additional text
    total = progress + trailer + retriever + exclude
    draw_text(win, additional_text, 17, "black", 170, 50)
    draw_text(win, f"{total} outcomes in total", 15, "#336699", 170, 550)
    # Calculate and display bar counts
    bar_height = 20
    text_offset = 10
    draw_text(win, f"{progress}", 14, "#336699", 125, 500 - bar_height * progress - text_offset)
    draw_text(win, f"{trailer}", 14, "#336699", 225, 500 - bar_height * trailer - text_offset)
    draw_text(win, f"{retriever}", 14, "#336699", 325, 500 - bar_height * retriever - text_offset)
    draw_text(win, f"{exclude}", 14, "#336699", 425, 500 - bar_height * exclude - text_offset)
    win.getMouse()  # Wait for a mouse click to close the window
    win.close()
render_graph(progress, trailer, retriever, exclude, total, additional_text)

