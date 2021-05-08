# The SubscriptionId in which to create
echo ("Start...")
$SubscriptionId = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Set the resource group name and location for our ADF instance
$resourceGroupName = "testResourceGroup-$(Get-Random)"
$adfInstanceName = "testadfInstance-$(Get-Random)"
$location = "eastus"
echo ("All variables assigned..")

# Set subscription and Connect-AzAccount
Set-AzContext -SubscriptionId $subscriptionId 
echo ("Azure Subscription set..")

# Register the Microsoft Azure Data Factory resource provider
Register-AzureRmResourceProvider -ProviderNamespace Microsoft.DataFactory
echo ("Registered the resource provider for Microsoft ADF instance..")

# Create a resource group
$resourceGroup = New-AzResourceGroup -Name $resourceGroupName -Location $location
echo ("ResourceGroup "+ $resourceGroupName +" has been created.")

# Create a blank AZURE DATA FACTORY instance
New-AzureRmDataFactoryV2 -ResourceGroupName $resourceGroupName -Name $adfInstanceName -Location $location

#Summary
echo ("Kudos, We have successfully created our Azure Data Factory - "+ $adfInstanceName +" through PowerShell!")
