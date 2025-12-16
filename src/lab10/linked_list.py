from typing import Any, Iterator, Optional


class Node:
    
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size: int = 0
    
    def append(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None:
            # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Если список не пуст
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        new_node = Node(value)
        
        if self.head is None:
            # Если список пуст
            self.head = new_node
            self.tail = new_node
        else:
            # Если список не пуст
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        if idx == 0:
            # Вставка в начало
            self.prepend(value)
            return
        elif idx == self._size:
            # Вставка в конец
            self.append(value)
            return
        
        # Вставка в середину
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        if idx == 0:
            # Удаление из начала
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            # Удаление из середины или конца
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            # current теперь указывает на элемент перед удаляемым
            if current.next == self.tail:
                # Если удаляем последний элемент
                self.tail = current
            
            current.next = current.next.next
        
        self._size -= 1
    
    def remove(self, value: Any) -> bool:
        if self.head is None:
            return False
        
        # Проверяем первый элемент
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return True
        
        # Ищем в остальной части списка
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                self._size -= 1
                return True
            current = current.next
        
        return False
    
    def __iter__(self) -> Iterator[Any]:
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        return self._size
    
    def __repr__(self) -> str:
        elements = list(self)
        return f"SinglyLinkedList({elements})"
    
    def visual_repr(self) -> str:
        parts = []
        current = self.head
        while current is not None:
            parts.append(f"[{current.value}]")
            current = current.next
        parts.append("None")
        return " -> ".join(parts)
    
    def get(self, idx: int) -> Any:
        if idx < 0 or idx >= self._size:
            raise IndexError(f"Index {idx} out of range for list of size {self._size}")
        
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value


if __name__ == "__main__":
    # Демонстрация работы односвязного списка
    print("=== Демонстрация SinglyLinkedList ===")
    lst = SinglyLinkedList()
    print(f"Пустой список: {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    print(f"Длина: {len(lst)}")
    
    # Добавление элементов
    lst.append(10)
    lst.append(20)
    lst.append(30)
    print(f"\nПосле append: {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Добавление в начало
    lst.prepend(5)
    print(f"\nПосле prepend(5): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Вставка по индексу
    lst.insert(2, 15)
    print(f"\nПосле insert(2, 15): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Получение элемента
    print(f"\nЭлемент по индексу 2: {lst.get(2)}")
    
    # Итерация
    print("\nИтерация по списку:")
    for item in lst:
        print(f"  {item}")
    
    # Удаление по значению
    lst.remove(20)
    print(f"\nПосле remove(20): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    
    # Удаление по индексу
    lst.remove_at(1)
    print(f"\nПосле remove_at(1): {lst}")
    print(f"Визуально: {lst.visual_repr()}")
    print(f"Длина списка: {len(lst)}")