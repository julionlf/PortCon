dcc_garch <- function(data,periods,
                      arma_alpha,arma_beta,
                      garch_alpha,garch_beta,
                      dcc_garch_alpha,dcc_garch_beta){
 
  # Import Libraries
  library(rugarch)
  library(rmgarch)
  
  # Read in file provided by user and eliminate date column
  #data <- read.csv(file,TRUE,',')
  drops <- c("Date")
  data <- data[ , !(names(data) %in% drops)]
  
  # Step 1: Specify Univariate-GARCH
  univariate_spec <- ugarchspec(
    mean.model = list(armaOrder = c(arma_alpha,arma_beta)),
    variance.model = list(garchOrder = c(garch_alpha,garch_beta),
                          model = "sGARCH"),
    distribution.model = "norm"
  )
  
  # Step 1: Specify DCC-GARCH
  n <- dim(data)[2]
  dcc_spec <- dccspec(uspec = multispec(replicate(n,univariate_spec)), 
                      dccOrder = c(dcc_garch_alpha,dcc_garch_beta), 
                      distribution = "mvnorm")
  
  # Fit DCC-GARCH Model
  dcc_fit <- dccfit(dcc_spec, data=data)
  
  # Forecast the DCC for the next period(s)
  forecasts <- dccforecast(dcc_fit, n.ahead = periods)
  
  # Store the covariance matrix
  sigma <- forecasts@mforecast$H
  sigma <- data.frame(sigma)
  return(sigma)
  
}