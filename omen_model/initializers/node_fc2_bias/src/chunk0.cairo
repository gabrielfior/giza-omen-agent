use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 3925, sign: true });
a.append(FP16x16 { mag: 10223, sign: false });
a.append(FP16x16 { mag: 8436, sign: false });
a.append(FP16x16 { mag: 11137, sign: true });
a.append(FP16x16 { mag: 11864, sign: false });
a.append(FP16x16 { mag: 9581, sign: true });
a.append(FP16x16 { mag: 8513, sign: true });
a.append(FP16x16 { mag: 1533, sign: true });
a.append(FP16x16 { mag: 10331, sign: false });
a.append(FP16x16 { mag: 5165, sign: false });
a.append(FP16x16 { mag: 11193, sign: true });
a.append(FP16x16 { mag: 9656, sign: true });
a.append(FP16x16 { mag: 1859, sign: false });
a.append(FP16x16 { mag: 2342, sign: false });
a.append(FP16x16 { mag: 1051, sign: true });
a.append(FP16x16 { mag: 10485, sign: true });
}