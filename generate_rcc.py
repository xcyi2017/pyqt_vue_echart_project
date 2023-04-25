import os

cu = "web/dist"
# print(cu)


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            L.append(os.path.join(root, file))
    return L


files = file_name(cu)
# print(files)
temp_str = '<file>App.ico</file>'
for i in files:
    tem = "/".join(i.split("\\"))
    temp_str = temp_str + "\n" + '''    <file>{}</file>'''.format(tem)

temp_str = '''<RCC>
  <qresource prefix="/">
    %s
  </qresource>
</RCC>
''' % temp_str
# print(temp_str)

with open("res.qrc", 'w', encoding="utf-8") as f:
    f.write(temp_str)

os.popen("pyrcc5.exe res.qrc -o ./ui/res_rc.py")
