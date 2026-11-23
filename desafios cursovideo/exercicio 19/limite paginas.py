class Book:
    def __init__(self, title:str, total_pages:int) -> str:
        self.title = title
        self.total_pages = max(1, total_pages)
        self.current_page = 1
        
        print(f"You opened the book '{self.title}', which has {self.total_pages} in total.\nYou are on Page 1.")
        
    def next_page(self, read:int) -> str:
        limit = self.current_page + read
        
        for n in range(self.current_page, limit):
            if self.__end_book():
                break
            
            if n != self.total_pages:
                print(f'Page{n} -> ', end='')
            else:
                print(f'Page{n}! ', end='')
                
            self.current_page = n +1
            
        if self.__end_book():
            print(f'You read the {self.total_pages} pages of the book. Congratulations!')
            
        else:
            print(f'You read {self.current_page -1} and now you are on page {self.current_page}')
        
    def __end_book(self) -> bool:
        return True if self.current_page > self.total_pages else False
        

b1 = Book('It a coisa', 20)
b1.next_page(17)
b1.next_page(3)