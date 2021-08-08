import math
import argparse


def verifica_Nones(t, p, P, n, i):
    n = 0
    args = [t, p, P, n, i]
    for a in args:
        if a is None:
            n += 1
    if n > 1:
        return False
    return True


def verifica_juros(i):
    if i is None:
        return False
    return True


def verifica_tipo(t):
    if t in ['annuity', 'diff']:
        return True
    return False


def verifica_diff(t, p):
    if t == 'annuity' or t == 'diff' and p is None:
        return True
    return False


def verifica_negativos(p, P, n, i):
    args = [p, P, n, i]
    for a in args:
        if a is None:
            continue
        else:
            if a < 0:
                return False
    return True


def verificador(i, t, p, P, n):
    resultados = [verifica_Nones(t, p, P, n, i), verifica_juros(i), verifica_tipo(t), verifica_diff(t, p),
                  verifica_negativos(p, P, n, i)]
    print(resultados)
    if not all(resultados):
        print('Incorrect parameters')
        exit()


parser = argparse.ArgumentParser()

parser.add_argument('--type', type=str)
parser.add_argument('--payment', type=int)
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

verificador(args.interest, args.type, args.payment, args.principal, args.periods)

i, n, P, p = args.interest / 1200, args.periods, args.principal, args.payment

if args.type == 'diff':
    total = 0
    for m in range(1, n + 1):
        diff = math.ceil((P / n) + i * (P - ((P * (m - 1)) / n)))
        total += diff
        print(f'Month {m}: payment is {diff}')
    print(f'\nOverpayment = {math.ceil(total - P)}')
elif args.type == 'annuity':
    if args.payment is None:
        p = math.ceil(P * (i * pow((1 + i), n)) / (pow((1 + i), n) - 1))
        print(f'Your monthly payment = {p}!')
    else:
        if args.principal is None:
            P = p / ((i * (pow((1 + i), n))) / (pow((1 + i), n) - 1))
            print(f'Your loan principal = {math.floor(P)}!')
        else:
            n = math.ceil(math.log(p / (p - i * P), 1 + i))
            years, months = n // 12, n % 12
            if years == 0:
                print(f'It will take {months} months to repay this loan!')
            elif months == 0:
                if years == 1:
                    print(f'It will take 1 year to repay this loan!')
                else:
                    print(f'It will take {years} years to repay this loan!')
            else:
                print(f'It will take {years} years and {months} months to repay this loan!')
    print(f'Overpayment = {math.ceil(p * n - P)}')
