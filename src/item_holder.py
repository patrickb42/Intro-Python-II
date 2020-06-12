def take_item(self):
    def func(item: str, src=None):
        if src is not None:
            try:
                src.drop_item(item)
            except Exception:
                print(f'error dropping having src {src} drop item {item}')
        self.items = self.items.set(item, 100)
    return func

def drop_item(self):
    def func(item, dest=None):
        self.items = self.items.discard(item)
        if dest is not None:
            dest.take_item(item)
    return func
