def collision(asteroids):
    i = 0
    N = len(asteroids) - 1

    while i < N:

        if asteroids[i] >= 0 and asteroids[i + 1] < 0:

            if asteroids[i] > -1 * asteroids[i + 1]:
                asteroids[i + 1] = 0
                i += 1

            elif asteroids[i] == -1 * asteroids[i + 1]:
                asteroids[i] = asteroids[i + 1] = 0
                i += 1

            else:
                asteroids[i] = asteroids[i + 1]
                asteroids[i + 1] = 0
                if i != 0:
                    i -= 1

        else:
            i += 1

    return [v for v in asteroids if v != 0]

if __name__ == "__main__":

    print(collision([5,10,-5]))
    print(collision([10,2,-5]))
    print(collision([8,-8]))
