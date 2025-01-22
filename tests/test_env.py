import getpass
import keyring

def test_env_variables():
    username = getpass.getuser()
    clientid = keyring.get_password("wow-clientid", username)
    clientsecret = keyring.get_password("wow-clientsecret", username)

    assert(username)
    assert(clientid)
    assert(clientsecret)