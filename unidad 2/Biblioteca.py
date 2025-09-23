import json
from pathlib import Path
from typing import Dict, Any, Optional


DEFAULT_BIBLIOTECA: Dict[str, Dict[str, Any]] = {
    "978-84-376-0494-7": {
        "título": "Cien años de soledad",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Realismo mágico", "Novela histórica"]
    },
    "978-84-204-1625-5": {
        "título": "Don Quijote de la Mancha",
        "autor": ["Miguel de Cervantes Saavedra"],
        "géneros": ["Novela de caballería", "Satira"]
    },
    "978-84-339-7962-7": {
        "título": "La casa de los espíritus",
        "autor": ["Isabel Allende"],
        "géneros": ["Realismo mágico", "Saga familiar"]
    },
    "978-84-06-12345-6": {
        "título": "El amor en los tiempos del cólera",
        "autor": ["Gabriel García Márquez"],
        "géneros": ["Novela romántica", "Realismo mágico"]
    }
}


JSON_PATH = Path(__file__).with_suffix('.json')


def cargar_biblioteca(path: Optional[Path] = None) -> Dict[str, Dict[str, Any]]:
    """Carga la biblioteca desde un archivo JSON. Si no existe, devuelve la biblioteca por defecto y la guarda."""
    if path is None:
        path = JSON_PATH
    if path.exists():
        try:
            with path.open('r', encoding='utf-8') as f:
                data = json.load(f)
                # Asegurar que las claves y valores tengan el formato esperado
                if isinstance(data, dict):
                    return data
        except Exception as e:
            print(f"Error al leer {path}: {e}")
    # Si no existe o hubo error, usamos la por defecto y la guardamos
    guardar_biblioteca(DEFAULT_BIBLIOTECA, path)
    return DEFAULT_BIBLIOTECA.copy()


def guardar_biblioteca(biblio: Dict[str, Dict[str, Any]], path: Optional[Path] = None) -> None:
    """Guarda la biblioteca en un archivo JSON con codificación UTF-8."""
    if path is None:
        path = JSON_PATH
    try:
        with path.open('w', encoding='utf-8') as f:
            json.dump(biblio, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(f"Error al guardar {path}: {e}")


def mostrar_info_por_isbn(biblioteca: Dict[str, Dict[str, Any]], isbn: str) -> None:
    info_libro = biblioteca.get(isbn)
    if info_libro is None:
        print(f"\nNo se encontró ningún libro con ISBN {isbn}.")
        return
    print(f"\nInformación del libro (ISBN {isbn}):")
    print(json.dumps(info_libro, ensure_ascii=False, indent=2))


def listar_isbns(biblioteca: Dict[str, Dict[str, Any]]) -> None:
    print("\nISBN disponibles:")
    for clave in biblioteca.keys():
        print("-", clave)


def agregar_libro(biblioteca: Dict[str, Dict[str, Any]], isbn: str, titulo: str, autores: list, generos: list) -> None:
    biblioteca[isbn] = {
        "título": titulo,
        "autor": autores,
        "géneros": generos
    }


def agregar_libro_interactivo(biblioteca: Dict[str, Dict[str, Any]]) -> None:
    # La versión interactiva fue eliminada para simplificar el script.
    # Si necesitas añadir libros desde la consola, usa la función `agregar_libro` desde otro script
    # o vuelve a implementar la entrada por `input()`.
    raise NotImplementedError("Funcionalidad interactiva deshabilitada.")


def mostrar_todos(biblioteca: Dict[str, Dict[str, Any]]) -> None:
    print("\nTodos los libros en la biblioteca:")
    for isbn, info in biblioteca.items():
        print(f"\nISBN {isbn}:")
        print(json.dumps(info, ensure_ascii=False, indent=2))


def main() -> None:
    """Carga la biblioteca desde el JSON (o crea el archivo por defecto) y muestra todos los libros.

    Para añadir libros programáticamente, importa `agregar_libro`, modifica el diccionario y
    llama a `guardar_biblioteca(biblioteca)`.
    """
    biblioteca = cargar_biblioteca()
    print(f"Biblioteca cargada desde: {JSON_PATH}")
    mostrar_todos(biblioteca)


if __name__ == "__main__":
    main()
