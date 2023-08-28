import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

root = ET.Element("Libros")

libro1 = ET.SubElement(root, "Libro")
titulo1 = ET.SubElement(libro1, "Titulo")
titulo1.text = "El Gran Gatsby"
autor1 = ET.SubElement(libro1, "Autor")
autor1.text = "F. Scott Fitzgerald"

libro2 = ET.SubElement(root, "Libro")
titulo2 = ET.SubElement(libro2, "Titulo")
titulo2.text = "1984"
autor2 = ET.SubElement(libro2, "Autor")
autor2.text = "George Orwell"

tree = ET.ElementTree(root)

# Crear un objeto minidom para formatear el XML
xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

# Guardar el XML formateado en un archivo
with open("libros.xml", "w") as f:
    f.write(xmlstr)