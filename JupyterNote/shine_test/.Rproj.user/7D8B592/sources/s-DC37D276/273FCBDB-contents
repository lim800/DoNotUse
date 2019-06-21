library('shiny')
library('ggplot2')
library('plotly')
options(shiny.port = 7776)
options(shiny.host = "127.0.0.1")
shinyApp(
  
  ui <- fluidPage(
    plotlyOutput("plotly", width = 400, height = 500)
    
    
  ), 
  server <- function(input, output, session) {
    output$plotly <- renderPlotly({
      mpg <- ggplot2::mpg
      ggplot(data =mpg, aes(x=displ, y=hwy, col=drv)) +geom_point()
      
    })
  }
  )