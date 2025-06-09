def customerSuccessBalancing(customerSuccess, customers, customerSuccessAway):
    available_cs = [cs for cs in customerSuccess if cs['id'] not in customerSuccessAway]
    available_cs.sort(key=lambda cs: cs['score'])
    customers.sort(key=lambda client: client['score'])
    cs_client_count = {cs['id']: 0 for cs in available_cs}
    cs_index = 0
    for client in customers:
        while cs_index < len(available_cs) and available_cs[cs_index]['score'] < client['score']:
            cs_index += 1
        if cs_index < len(available_cs):
            cs_client_count[available_cs[cs_index]['id']] += 1
    max_clients = max(cs_client_count.values(), default=0)
    top_cs = [cs_id for cs_id, count in cs_client_count.items() if count == max_clients]
    return top_cs[0] if len(top_cs) == 1 else 0

if __name__ == "__main__":
    cs = [
        {"id": 1, "score": 60},
        {"id": 2, "score": 20},
        {"id": 3, "score": 95},
        {"id": 4, "score": 75}
    ]
    clients = [
        {"id": 1, "score": 90},
        {"id": 2, "score": 20},
        {"id": 3, "score": 70},
        {"id": 4, "score": 40},
        {"id": 5, "score": 60},
        {"id": 6, "score": 10}
    ]
    away = [2, 4]
    result = customerSuccessBalancing(cs, clients, away)
    print("Resultado:", result)
