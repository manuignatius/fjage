#!/bin/sh

# fjage version
VERSION=1.3.1

# create the folder structure
mkdir -p build/libs etc logs samples

# download necessary JARs
cd build/libs
curl -O http://search.maven.org/remotecontent?filepath=com/github/org-arl/fjage/$VERSION/fjage-$VERSION.jar
curl -O http://search.maven.org/remotecontent?filepath=org/codehaus/groovy/groovy-all/2.1.3/groovy-all-2.1.3.jar
curl -O http://search.maven.org/remotecontent?filepath=org/apache/commons/commons-lang3/3.1/commons-lang3-3.1.jar
curl -O http://search.maven.org/remotecontent?filepath=jline/jline/2.10/jline-2.10.jar
#curl -O http://search.maven.org/remotecontent?filepath=uk/com/robust-it/cloning/1.9.0/cloning-1.9.0.jar
#curl -O http://search.maven.org/remotecontent?filepath=org/objenesis/objenesis/1.2/objenesis-1.2.jar
cd ../..

# download init scripts and logging configuration
cd etc
curl -O https://raw.github.com/org-arl/fjage/master/etc/initrc.groovy
cd ..

#TODO: Move from dev dir to master once done
# download sample agents
cd samples
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/01_hello.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/02_ticker.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/03_weatherStation.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/03_weatherRequest.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/WeatherForecastReqMsg.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/04_weatherStation.groovy
curl -O https://raw.github.com/manuignatius/fjage/dev/samples/04_weatherRequest.groovy
cd ..

# download startup script
curl -O https://raw.github.com/manuignatius/fjage/dev/fjage.sh
chmod a+x fjage.sh