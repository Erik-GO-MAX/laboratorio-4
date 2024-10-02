class ListaDeTareas:
    def _init_(self):
        """Inicializa la lista de tareas vacía."""
        self.tareas = []

    def agregar_tarea(self, tarea):
        """Agrega una tarea a la lista de tareas y muestra un mensaje de confirmación."""
        self.tareas.append(tarea)
        print(f"La tarea '{tarea}' ha sido agregada.")

    def eliminar_tarea(self, tarea):
        """Elimina una tarea de la lista si está presente, y muestra un mensaje de confirmación o error."""
        if tarea in self.tareas:
            self.tareas.remove(tarea)
            print(f"La tarea '{tarea}' ha sido eliminada.")
        else:
            print(f"La tarea '{tarea}' no se encuentra en la lista.")

    def mostrar_tareas(self):
        """Muestra todas las tareas pendientes o indica que no hay tareas."""
        if self.tareas:
            print("Tareas pendientes:")
            for tarea in self.tareas:
                print(f"- {tarea}")
        else:
            print("No hay tareas pendientes.")
