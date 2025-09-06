class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack_top = [] #history of visited pages
        self.stack_bottom = [] #to keep track when we move forward

        self.stack_top.append(homepage)

    def visit(self, url: str) -> None:
        self.stack_top.append(url)
        # print("initial", self.stack_top)
        self.stack_bottom = [] #clear the forward history since we are visiting a new page
        

    def back(self, steps: int) -> str:
        while steps and len(self.stack_top) > 1:#you can't go back after the homepage
            remove = self.stack_top.pop()
            self.stack_bottom.append(remove)
            # print("current", self.stack_top)
            # print("back", self.stack_bottom)
            steps -= 1
        
        return self.stack_top[-1] #peep not pop
        

    def forward(self, steps: int) -> str:

        while steps and self.stack_bottom:
            remove = self.stack_bottom.pop()
            self.stack_top.append(remove)
            steps -= 1

        return self.stack_top[-1] #return the current page
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)