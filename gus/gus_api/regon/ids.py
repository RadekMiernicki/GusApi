import uuid

# make UUID based on current time and host ID
id1 = uuid.uuid1(node=1001)

id2 = uuid.uuid5(namespace=uuid.NAMESPACE_URL, name='ecoloop')


print(id1)
print(id2.hex)