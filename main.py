import guiCalculator
import math
import calculatorAdsDataBase
import advertising


ads = advertising.advertising(['bakery.png','TAN.png','AndersonLogs.png','naturallog.png','e.png','roots.png','signs.png'])

database = calculatorAdsDataBase.cADB()

calc = guiCalculator.guiCalculator(database,ads)

