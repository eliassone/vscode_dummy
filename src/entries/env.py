import os

def main():
    env = os.environ.get('ENVIRONMENT')
    print(f'Current environment: {env}')

if __name__ == '__main__':
    main()