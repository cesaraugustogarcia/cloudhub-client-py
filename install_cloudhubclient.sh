echo "export CLOUDHUBCLIENT_HOME=~/.cloudhubclient" >> $HOME/.profile
source $HOME/.profile

echo "alias cloudhub='python $CLOUDHUBCLIENT_HOME/cloudhubClient.py'" >> $HOME/.profile
source $HOME/.profile

if [ ! -d "$CLOUDHUBCLIENT_HOME" ]; then
  mkdir $CLOUDHUBCLIENT_HOME
fi

cp -rf . $CLOUDHUBCLIENT_HOME

chmod +x $CLOUDHUBCLIENT_HOME/cloudhubClient.py
source $HOME/.profile