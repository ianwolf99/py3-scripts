import ldap
import ldap.modlist as modlist

LDAP_URI = "ldap://10.0.2.15:389/"
BIND_TO = "dc=localdomain,dc=loc"
BASE_DN = 'ou=users,dc=localdomain,dc=loc'
SEARCH_FILTER = '(objectclass=person)'
SEARCH_FILTER = ['sn']

if __name__ == '__main__':
    l = ldap.initialize(LDAP_URI)
    l.simple_bind(BIND_TO)
    result = l.search_s(BASE_DN ,ldap.SCOPE_SUBTREE,SEARCH_FILTER,SEARCH_FILTER)
    print(result)