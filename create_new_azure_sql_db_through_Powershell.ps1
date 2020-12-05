# The SubscriptionId in which to create
echo ("Start...")
$SubscriptionId = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Set the resource group name and location for our server
$resourceGroupName = "testResourceGroup-$(Get-Random)"
$location = "eastus"

# Set an admin login and password for our server
$adminSqlLogin = "TestLogin"
$password = "TestPassword123!"

# Set server name - the logical server name has to be unique in the system
$serverName = "testserver-$(Get-Random)"

# The Test database name
$databaseName = "TestDatabase"

# If both startIP and endIP is equal to '0.0.0.0', means 'Allow Azure services and resources to access this server' set to 'Yes'
# The ip address range that you want to allow to access our server
$startIp = "0.0.0.0"
$endIp = "0.0.0.0"
echo ("All variables assigned..")

# Set subscription and Connect-AzAccount
Set-AzContext -SubscriptionId $subscriptionId 
echo ("Azure Subscription set..")

# Create a resource group
$resourceGroup = New-AzResourceGroup -Name $resourceGroupName -Location $location
echo ("ResourceGroup "+ $resourceGroupName +" has been created.")

# Create a server with a system wide unique server name
$server = New-AzSqlServer -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -Location $location `
    -SqlAdministratorCredentials $(New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $adminSqlLogin, $(ConvertTo-SecureString -String $password -AsPlainText -Force))
echo ("Logical Server "+ $serverName +" has been created.")

# Create a server firewall rule that allows access from the specified IP range
$serverFirewallRule = New-AzSqlServerFirewallRule -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -FirewallRuleName "AllowedIPs" -StartIpAddress $startIp -EndIpAddress $endIp
echo ("Server Firewall set..")	

# Create a blank database with an basic performance level
$database = New-AzSqlDatabase  -ResourceGroupName $resourceGroupName `
    -ServerName $serverName `
    -DatabaseName $databaseName `
    -RequestedServiceObjectiveName "basic" `

#Summary
echo ("Kudos, We have successfully created our Azure SQL DB - "+ $databaseName +" through PowerShell!")
