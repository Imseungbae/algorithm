answer = ""
part = ["mislav", "stanko", "mislav", "ana"]
comp = ["stanko", "ana", "mislav"]

part.sort()
comp.sort()

for idx in range(len(part)):
    if part[idx] != comp[idx] or idx >= len(comp):
        answer = part[idx]
        break

print(answer)

    
