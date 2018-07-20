import externs

p = externs.labelAndComposite("test.jpg", "blah.txt", "+10", "+50", "output.jpg")
out = p.stdout.readlines()
print(out)

p = externs.shell("ps -ef | grep python")
out = p.stdout.readlines()
print(out)