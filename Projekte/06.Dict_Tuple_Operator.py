def status_norm(n):
    if n == 1:
        return "OK"
    elif n == 2:
        return "WARN"
    else:
        return "??"

def action_norm(a):
    if a == 0:
        return "GO"
    elif a == 1:
        return "STOP"
    else:
        return "??"


def status_dict(n):
    return {1: "OK", 2: "WARN"}.get(n, "??")

def action_tuple(a):
    acts = ("GO", "STOP")
    return acts[a] if 0 <= a < len(acts) else "??"

def main():
    nums = [1, 2, 5]
    acts = [0, 1, 3]

    print("=== STATUS ===")
    for n in nums:
        print(f"{n}: norm={status_norm(n)}, dict={status_dict(n)}")

    print("\n=== ACTION ===")
    for a in acts:
        print(f"{a}: norm={action_norm(a)}, tuple={action_tuple(a)}")


if __name__ == "__main__":
    main()
