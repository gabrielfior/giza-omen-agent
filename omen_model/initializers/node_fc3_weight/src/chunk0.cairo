use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 1863, sign: true });
a.append(FP16x16 { mag: 3499, sign: true });
a.append(FP16x16 { mag: 8992, sign: false });
a.append(FP16x16 { mag: 15817, sign: true });
a.append(FP16x16 { mag: 2333, sign: false });
a.append(FP16x16 { mag: 13200, sign: false });
a.append(FP16x16 { mag: 2377, sign: false });
a.append(FP16x16 { mag: 618, sign: true });
a.append(FP16x16 { mag: 11972, sign: false });
a.append(FP16x16 { mag: 5666, sign: false });
a.append(FP16x16 { mag: 15067, sign: true });
a.append(FP16x16 { mag: 10736, sign: false });
a.append(FP16x16 { mag: 12978, sign: true });
a.append(FP16x16 { mag: 9883, sign: false });
a.append(FP16x16 { mag: 4080, sign: true });
a.append(FP16x16 { mag: 11779, sign: true });
}