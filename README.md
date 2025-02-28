# Competitive Programming ![WakaTime](https://wakatime.com/badge/user/3dffa020-4a1a-4dcc-8526-a337c2321c39/project/018eaf79-1703-45fc-b3af-4e3720f27cb2.svg?style=flat-square)

> Я просто хочу пройти алгоритмический собес 🥺

## Алгоритмы

- **KMP** — поиск подстроки в строке за O(m + n). Встретился в [28](https://github.com/MarshalX/competitive-programming/blob/6b2a5be0d03e7b7219645f8841f24beba80f036c/main.cpp). [Брутфорс](https://github.com/MarshalX/competitive-programming/blob/614c1ef638e04804b348ad9463c20f4e8378e32f/main.cpp) ушёл в TL. Алгос списал с псевдокода на вики: [Knuth–Morris–Pratt algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm).
- **Prefix sum** — [быстрый ответ](https://github.com/MarshalX/competitive-programming/blob/b86ddc27fc22820f2fc1d3e4008ddc2c2471e454/main.cpp) на множество вопросов "Какая сумма на подмассиве от L до R?" (`pref[0] = a[0]; pref[i] = pref[i - 1] + a[i]. Q: pref[r] - pref[l - 1] или pref[r] если l == 0`). Точ в точ задача [303](https://github.com/MarshalX/competitive-programming/blob/b815c2340153d415895e18e8899f0a226c08de54/main.cpp). Интересное и легкое усложнение задачи в [724](https://github.com/MarshalX/competitive-programming/blob/a507ae4e8671bd6b49eaaa2c9a5e9c8d69b1f5d3/main.cpp).
- **Kadane's algorithm** — подмассив с [наибольшей суммой](https://github.com/MarshalX/competitive-programming/blob/7ab975a6852e5a156f724c54e15bbf8316dcc0d7/main.cpp) (`tSum += a[i]; tSum = max(tSum, a[i]); res = max(res, tSum)`).

## Ссылки на почитать

### Списки задач
- [NeetCode](https://neetcode.io/practice?tab=neetcode150)
- [Blind 75](https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions)
- [Grind 75](https://www.techinterviewhandbook.org/grind75)
- [AlgoMap](https://algomap.io/)
- [CSES Problem Set](https://cses.fi/problemset)

### Сайты с темами
- [The Ultimate Topic List](https://youkn0wwho.academy/topic-list)
- [brestprog](https://brestprog.by/topics/)
- [algorithm gitbook](https://liuzhenglaichn.gitbook.io/algorithm)
- [USACO Guide](https://usaco.guide/)

### Конкретные темы
- [x] [Maximum subarray problem (Kadane's algorithm)](https://en.wikipedia.org/wiki/Maximum_subarray_problem). LeetCode [53](https://leetcode.com/problems/maximum-subarray/)
- [ ] [Sliding Window Technique](https://quanticdev.com/algorithms/dynamic-programming/sliding-window/)
- [x] [Префиксные суммы. XOR. Задачи на запросы](https://brestprog.by/topics/prefixsums/)
- [x] [Полное бинарное дерево. Куча. Очередь с приоритетом](https://brestprog.by/topics/heap/)
- [ ] [Hamming weight](https://en.wikipedia.org/wiki/Hamming_weight). LeetCode [191](https://github.com/MarshalX/competitive-programming/blob/b05daa0e7889065671c62d4a3267d08e5f94eea7/main.cpp) 
- [ ] [Custom impl of `__builtin_popcount`](https://stackoverflow.com/questions/52161596/why-is-builtin-popcount-slower-than-my-own-bit-counting-function/52161813) 
- [ ] [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance)
- [ ] [How to count leading zeros in integer (`__builtin_clz` and pure impls)](https://stackoverflow.com/questions/23856596/how-to-count-leading-zeros-in-a-32-bit-unsigned-integer)

## Ссылки на посмотреть
- [Четыре задачи на два указателя](https://youtu.be/MyWNZJ10zIU)
- [Алгоритм Кнута-Морриса-Пратта](https://youtu.be/7g-WEBj3igk)
- [Динамическое программирование это просто](https://youtu.be/GOF4VUi4nGU)
- [Задача о рюкзаке. Динамическое программирование](https://youtu.be/AgM-w6QuIHQ)
- [Прямая и обратная польская нотация](https://youtu.be/sC566vzV9B0)
- [Популярная в собеседованиях гугл задача. Разбор и решение (Guess the word 843 на LeetCode)](https://youtu.be/pJNd7AzIWGc)
- [Хитрая задача на Стек](https://youtu.be/-59FbGWsCgI)
- [Поиск Знаменитости. Метод двух указателей](https://youtu.be/xGvQN_g-JCI)
- [Динамическое Программирование: Количество Уникальных Путей](https://youtu.be/GhiRlhPlJ9Q)
- [What is Bitmasking](https://youtu.be/7FmL-WpTTJ4)
- [Bitwise Operations tutorial #1 | XOR, Shift, Subsets](https://youtu.be/xXKL9YBWgCY)
- Плейлист [АиСД year2020 s1](https://youtube.com/playlist?list=PLrS21S1jm43jz48qjdfYNpuIPgL3lNJ_o)
- Что такое sliding window: [Solve subarray problems FASTER (using Sliding Windows)](https://youtu.be/GcW4mgmgSbw)
- Что такое dynamic programming: [Mastering Dynamic Programming - How to solve any interview problem (Part 1)](https://youtu.be/Hdr64lKQ3e4)
- [Linked List Cycle - Floyd's Tortoise and Hare](https://youtu.be/gBTe7lFR3vc)
- Найти позицию начала цикла (`len(head -> cycle_start) == len(equal_pointers -> cycle_start)`) [Floyd's Cycle Detection](https://youtu.be/wjYnzkAhcNk)
- [How Dijkstra's Algorithm Works](https://youtu.be/EFg3u_E6eHU)
