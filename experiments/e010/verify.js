// Compare checked-in result against executable analytical model; Node >= 18.
'use strict';
const assert=require('node:assert/strict');
const fs=require('node:fs');
const path=require('node:path');
const {execute,validate}=require('./run');
assert.deepStrictEqual(Object.values(validate()),Array(Object.keys(validate()).length).fill(true));
const actual=execute();
const stored=JSON.parse(fs.readFileSync(path.join(__dirname,'RESULT.json'),'utf8'));
assert.deepStrictEqual(actual,stored);
console.log('E010 synthetic output and 9 analytic consistency tests verified');
