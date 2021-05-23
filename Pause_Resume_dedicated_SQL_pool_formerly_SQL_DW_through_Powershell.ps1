# The SubscriptionId in which to use
echo ("Start...")
$SubscriptionId = 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

# Set subscription and Connect-AzAccount
Set-AzContext -SubscriptionId $subscriptionId 
echo ("Azure Subscription set..")

# NOTE : If ServerName is testservernameXYZ.database.windows.net, then in our powershell cmds, we need to provide the server name as testservernameXYZ.
# Assign the variables for our dedicated SQL pool (formerly SQL DW)
$resourceGroupName = "test-resourceGroupName"
$serverName = "test-serverName"
$databaseName = "test-databaseName"
echo ("All variables assigned..")

# To Pause compute of dedicated SQL pool (formerly SQL DW)
Suspend-AzSqlDatabase –ResourceGroupName $resourceGroupName –ServerName $serverName –DatabaseName $databaseName
echo ("Paused compute of dedicated SQL pool (formerly SQL DW)..")

# To Resume compute of dedicated SQL pool (formerly SQL DW)
Resume-AzSqlDatabase –ResourceGroupName $resourceGroupName –ServerName $serverName –DatabaseName $databaseName
echo ("Resumed compute of dedicated SQL pool (formerly SQL DW)..")