import traceback
from java.io import FileInputStream

def changeTargets():

	propInputStream = FileInputStream("restart.properties")
	configProps = Properties()
	configProps.load(propInputStream)
	userName = configProps.get("userName")
	password = configProps.get("password")
	adminUrl = configProps.get("admin.Url")
	totalDsCount = configProps.get("total.Ds.Count")
	
	TargetMBean = Class.forName("weblogic.management.configuration.TargetMBean")	
	
	nullTarget = jarray.array([], TargetMBean)
		

	connect(userName,password,adminUrl)
	edit()
	startEdit()
	print '======================================================================'
	print 'Existing domain info.....'
	print ''
	print cmo
	print '======================================================================'
	
	allJDBCResources = cmo.getJDBCSystemResources()
	
	print '======================================================================'
	print 'Untargeting all data sources.....'
	for jdbcResource in allJDBCResources:
		#Listing all data sources
		dsname = jdbcResource.getName()
		#print dsname, jdbcResource.getJDBCResource().getJDBCDataSourceParams().getJNDINames()[0], jdbcResource.getJDBCResource().getJDBCDriverParams().getUrl()
		#print jdbcResource.getTargets()
		#print ''
		
		jdbcResource.setTargets(nullTarget)
	print '======================================================================'
	save()
	activate()
	
	
	edit()
	startEdit()
	print '======================================================================'
	print 'Targeting all data sources.....'
	for jdbcResource in allJDBCResources:
		#Listing all data sources
		dsname = jdbcResource.getName()
		#print dsname, jdbcResource.getJDBCResource().getJDBCDataSourceParams().getJNDINames()[0], jdbcResource.getJDBCResource().getJDBCDriverParams().getUrl()
		#print jdbcResource.getTargets()
		#print ''
		
		target = cmo.lookupTarget('AdminServer')
		#print target
		targetArray = jarray.array([target], TargetMBean)
		#print targetArray
		jdbcResource.setTargets(targetArray)
		
	print '======================================================================'
	save()
	activate()
	



def main():
	print ''
	print '======================================================================'
	print 'UnTargeting and Targeting of the DataSources has started.....'
	print '======================================================================'
		
	
	try:
	 changeTargets()
	except:
		print '>>> traceback <<<'
		traceback.print_exc()
		undo()
		
		print '>>> end of traceback <<<'
		
	print '======================================================================'
	print 'UnTrageting and Targeting of the DataSources has been completed !!!'
	print '======================================================================'
	print ''
	disconnect()
	exit()
 
main()

