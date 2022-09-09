# Script: Ops 301d5 Ops Challenge: Class 08
# Author: Dean Weiss
# Date of latest revision: 08 Sept 2022
# Purpose: Write a Powershell script that adds the below person to AD.
# Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. # Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com

# main

New-ADUser -Name "Franz Ferdinand" -Department "TPS Reporting Lead" -Company "GlobX USA" -City "Springfield, OR" -Department "TPS Department" -EmailAddress "ferdi@GlobeXpower.com."

# end