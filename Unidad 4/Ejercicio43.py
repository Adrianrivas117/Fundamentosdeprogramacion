# -*- coding: utf-8 -*-

#Agregar un atributo al objeto Alumno de Edad. Si es mayor de edad que imprima un mensaje
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)

class Alumno:
    """Representa a un alumno con nombre y edad."""

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        # Atributo edad solicitado
        self.edad = edad

        # Comprobación: si es mayor de 18, imprimimos el mensaje
        if isinstance(self.edad, (int, float)) and self.edad > 18:
            print(f"{self.nombre}: mayor de edad")

    def es_mayor_de_edad(self) -> bool:
        """Devuelve True si el alumno es mayor de edad (>18)."""
        try:
            return self.edad > 18
        except Exception:
            return False


if __name__ == "__main__":
    # Ejemplos de uso
    a1 = Alumno("Ana", 20)   # imprimirá: Ana: mayor de edad
    a2 = Alumno("Luis", 17)  # no imprimirá nada
    a3 = Alumno("María", 18) # 18 no > 18, no imprimirá

    # Salida adicional de verificación
    print(f"{a1.nombre} tiene {a1.edad} años -> mayor? {a1.es_mayor_de_edad()}")
    print(f"{a2.nombre} tiene {a2.edad} años -> mayor? {a2.es_mayor_de_edad()}")
    print(f"{a3.nombre} tiene {a3.edad} años -> mayor? {a3.es_mayor_de_edad()}")

        
class Alumno:
    """Representa a un alumno con nombre y edad."""

    def __init__(self, nombre: str, edad: int):
        self.nombre = nombre
        # Atributo edad solicitado
        self.edad = edad

        # Comprobación: si es mayor de 18, imprimimos el mensaje
        if isinstance(self.edad, (int, float)) and self.edad > 18:
            print(f"{self.nombre}: mayor de edad")

    def es_mayor_de_edad(self) -> bool:
        """Devuelve True si el alumno es mayor de edad (>18)."""
        try:
            return self.edad > 18
        except Exception:
            return False


if __name__ == "__main__":
    # Ejemplos de uso
    a1 = Alumno("Ana", 20)   # imprimirá: Ana: mayor de edad
    a2 = Alumno("Luis", 17)  # no imprimirá nada
    a3 = Alumno("María", 18) # 18 no > 18, no imprimirá

    # Salida adicional de verificación
    print(f"{a1.nombre} tiene {a1.edad} años -> mayor? {a1.es_mayor_de_edad()}")
    print(f"{a2.nombre} tiene {a2.edad} años -> mayor? {a2.es_mayor_de_edad()}")
    print(f"{a3.nombre} tiene {a3.edad} años -> mayor? {a3.es_mayor_de_edad()}")
# -*- coding: utf-8 -*-



class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        self.resize(350, 180)

        # ------------------ Widgets ------------------
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")

        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        # Botón Limpiar (opcional)
        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # ------------------ Layout -------------------
        form_layout = QVBoxLayout()

        # Nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)

        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Ruta del archivo donde se guardarán los datos
        self.ruta_archivo = Path("alumnos.txt")

    # -------------------------------------------------
    def guardar_alumno(self):
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()

        if not nombre or not carrera:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar tanto el nombre como la carrera.",
            )
            return

        linea = f"{nombre} – {carrera}\n"

        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        QMessageBox.information(
            self,
            "Guardado",
            f"Alumno guardado correctamente en '{self.ruta_archivo}'.",
        )
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.nombre_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())