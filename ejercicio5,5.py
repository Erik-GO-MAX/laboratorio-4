class Album:
    def _init_(self):
        """Inicializa el álbum con una lista vacía de fotos."""
        self.fotos = []

    def agregar_foto(self, foto):
        """Agrega una foto al álbum y muestra un mensaje de confirmación."""
        self.fotos.append(foto)
        print(f"La foto '{foto}' ha sido agregada al álbum.")

    def eliminar_foto(self, foto):
        """Elimina una foto de la lista si está presente, y muestra un mensaje de confirmación o error."""
        if foto in self.fotos:
            self.fotos.remove(foto)
            print(f"La foto '{foto}' ha sido eliminada del álbum.")
        else:
            print(f"La foto '{foto}' no se encuentra en el álbum.")

    def mostrar_fotos(self):
        """Muestra todas las fotos en el álbum o indica que está vacío."""
        if self.fotos:
            print("Fotos en el álbum:")
            for foto in self.fotos:
                print(f"- {foto}")
        else:
            print("El álbum está vacío.")