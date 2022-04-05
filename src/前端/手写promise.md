# Promise
```js
class Promsie {
    constructor(fn) {
        //三个状态
        this.status = 'pending',
        this.resolve = undefined;
        this.reject = undefined;
        let resolve = value => {
            if (this.status === 'pending') {
                this.status = 'resolved';
                this.resolve = value;
            }
        };
        let reject = value => {
            if (this.status === 'pending') {
                this.status = 'rejected';
                this.reject = value;
            }
        }
        try {
            fn(resolve, reject)
        } catch (e) {
            reject(e)
        }
    }
    then(onResolved, onRejected) {
        switch (this.status) {
            case 'resolved': onResolved(this.resolve); break;
            case 'rejected': onRejected(this.resolve); break;
            default:
        }
    }

}
```

# Promise.all
```js
   function promiseAll(promises) {
            if (!Array.isArray(promises)) {
                throw new Error("promises must be an array")
            }
            return new Promise(function (resolve, reject) {

                let promsieNum = promises.length;
                let resolvedCount = 0;
                let resolveValues = new Array(promsieNum);
                for (let i = 0; i < promsieNum; i++) {
                    Promise.resolve(promises[i].then(function (value) {
                        resolveValues[i] = value;
                        resolvedCount++;
                        if (resolvedCount === promsieNum) {
                            return resolve(resolveValues)
                        }
                    }, function (reason) {
                        return reject(reason);
                    }))

                }
            })
        }
```

# Promise.race
```js
 function promiseRace(promises) {
            if (!Array.isArray(promises)) {
                throw new Error("promises must be an array")
            }
            return new Promise(function (resolve, reject) {
                promises.forEach(p =>
                    Promise.resolve(p).then(data => {
                        resolve(data)
                    }, err => {
                        reject(err)
                    })
                )
            })
        }
```