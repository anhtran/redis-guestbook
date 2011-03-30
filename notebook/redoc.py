# anhtran [at] Studio Moon9
# twitter.info

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
#r.set('global:nextPostId', '0')


def saveRedis(data):
    # data[0] => username
    # data[1] => message
    next = r.incr('global:nextPostId')
    r.set('pid:' + str(next) + ':username', data[0])
    r.set('pid:' + str(next) + ':message', data[1])
    r.rpush('user:' + str(data[0]) + ':posts', next)


def getRedis(id=None, number=None, user=None):
    # id = 99 => id of a single post
    # number = 100 => latest 100 posts
    # user = 101 => user_id
    data = []
    if id:
        data.append(r.get('pid:' + str(id) + ':username'))
        data.append(r.get('pid:' + str(id) + ':message'))
        return data
    elif number:
        current = r.get('global:nextPostId')
        bef = int(current)-int(number)
        aft = int(current)+1
        if bef >= 0:
            for i in range(bef, aft):
                sub = []
                sub.append(r.get('pid:' + str(i) + ':username'))
                sub.append(r.get('pid:' + str(i) + ':message'))
                data.append(sub)
            return data
        else:
            for i in range(1, aft):
                sub = []
                sub.append(r.get('pid:' + str(i) + ':username'))
                sub.append(r.get('pid:' + str(i) + ':message'))
                data.append(sub)
            return data
    elif user:
        posts = r.lrange('user:' + str(user) + ':posts', 0, -1)
        for i in posts:
            sub = []
            sub[0].append(r.get('pid:' + str(i) + ':username'))
            sub[1].append(r.get('pid:' + str(i) + ':message'))
            data.append(sub)
        return data
            
