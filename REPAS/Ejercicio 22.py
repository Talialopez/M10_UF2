import xml.etree.ElementTree as ET

def creacion_xml():
    root  = ET.Element('students')

    for i in range(5):
        student = ET.SubElement(root, 'student')

        student.set('id', 'student_' + str(i+1))

        name = ET.SubElement(student, 'name')
        name.text = 'Nombre_' + str(i+1)

        surname = ET.SubElement(student, 'surname')
        surname.text = 'Apellido_' + str(i+1)

        email = ET.SubElement(student, 'email')
        email.text = 'email' + str(i+1) + '@example.com'

        dni = ET.SubElement(student, 'dni')
        dni.text = 'DNI' + str(i+1)

    tree = ET.ElementTree(root)
    ET.dump(root)
    ET.indent(tree)
    tree.write('students.xml')

    with open('students.xml', 'r') as file:
        print(file.read())

creacion_xml()
