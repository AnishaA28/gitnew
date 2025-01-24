"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from datetime import datetime


class ExampleState(rx.State):
    colors: list[str]=[
        "black",
        "red",
        "pink",
        "green",
        "blue",
    ]

    index: int=0

    def next_color(self):
        self.index=(self.index+1) % len(self.colors)

    @rx.var
    def color(self) -> str:
        return self.colors[self.index]  

def first_text():
        return rx.text("Introduction",class_name="first-css-class")     

def second_text():
        return rx.text("Reflex is an open-source framework for quickly building beautiful, interactive web applications in pure Python.",class_name=".second-css-class")
  
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")




   

def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.box(
                  rx.box(rx.heading("Hello, World!", size="4", text_align="center",
                             on_click =ExampleState.next_color,color=ExampleState.color),
                  rx.text("Have a nice day", font_size="2em", text_align="center"),
        text_align="center",
        padding="2em",
        color="blue",
        border_radius="15px",
        border_width="thick"
        
        ),
        rx.text(
            first_text(),second_text(),
        style = {".first-css-class": {
        "font_family": "Georgia, serif",
        "font_size": "2em",
        "font_weight": "bold",
        "color": "black",
    },
    ".second-css-class": {
        "background_color": "lightgray",
        "font_size": "1.2em",
        "padding": "10px",
    },   } ),
          


        rx.box(
            rx.text("The Structure of REFLEX App", text_align="center"),  # Ensure non-empty, static content
            width="60%",  # Static width
            height="150px",  # Static height
            font_weight= "bold",
            margin="auto",
            padding="1em",
            border="1px solid #ccc",
            border_radius="8px",
            background_color="#f9f9f9",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.1)",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        # Content below the box
        rx.box(
            rx.text(
                "This is some static content below the box.",
                font_size="1.2em",
                text_align="center",
                
            ),
           ),
        rx.box(
            rx.container(
            rx.card("This content is constrained to a max width of 448px",
            width="100%",),
            size="2",
            ),
            background="blue",
            width="100%",
            ),
           
        

        rx.flex(
            rx.card("Card 1",color_scheme="red"),
            rx.card("Card 2"),
            rx.card("Card 3"),
            rx.card("Card 4"),
            rx.card("Card 5"),
            rx.card("Card 6"),
            rx.card("Card 7"),
            rx.card("Card 8"),
            rx.card("Card 9"),
            rx.card("Card 10"),
            spacing="2",
            flex_wrap="wrap",
            width="100%",
            
        ),
        rx.scroll_area(
        rx.flex(
        rx.text(
            """Three fundamental aspects of typography are legibility, readability, and
        aesthetics. Although in a non-technical sense “legible” and “readable”
        are often used synonymously, typographically they are separate but
        related concepts.""",
        ),
        rx.text(
            """Legibility describes how easily individual characters can be
        distinguished from one another. It is described by Walter Tracy as “the
        quality of being decipherable and recognisable”. For instance, if a “b”
        and an “h”, or a “3” and an “8”, are difficult to distinguish at small
        sizes, this is a problem of legibility.""",
        ),
        rx.text(
            """Typographers are concerned with legibility insofar as it is their job to
        select the correct font to use. Brush Script is an example of a font
        containing many characters that might be difficult to distinguish. The
        selection of cases influences the legibility of typography because using
        only uppercase letters (all-caps) reduces legibility.""",
        ),
        direction="column",
        spacing="4",
    ),
    type="always",
    scrollbars="vertical",
    style={"height": 180},
        ),
        
        rx.box(rx.button(
            rx.icon(tag="heart"),  
            "Like",  
            color_scheme="red",  
            icon_align="center"  
        ),
            style={
            "display": "flex",           
            "justify_content": "center", 
            "align_items": "center",    
            "height": "100vh",          
            }),
            rx.text(f"The current date and time is.: {datetime.now()}", text_align="center"),
            margin_top="1em",
            width="80%",
            margin="auto",
            padding="2em",
    spacing="90px",
        
                           
),       

            
       
        
    
        
    


app = rx.App()
app.add_page(index)
