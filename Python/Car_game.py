from livewires import games

games.init(screen_width=800, screen_height=600, fps=60)

background = games.load_image("Texture.jpg", transparent=False)
games.screen.background = background

games.screen.mainloop()
