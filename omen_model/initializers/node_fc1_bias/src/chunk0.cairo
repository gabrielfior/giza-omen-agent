use orion::numbers::{FixedTrait, FP16x16};

fn compute(ref a: Array<FP16x16>) {
a.append(FP16x16 { mag: 15355, sign: false });
a.append(FP16x16 { mag: 2186, sign: true });
a.append(FP16x16 { mag: 10412, sign: true });
a.append(FP16x16 { mag: 22535, sign: true });
a.append(FP16x16 { mag: 20463, sign: true });
a.append(FP16x16 { mag: 4535, sign: true });
a.append(FP16x16 { mag: 21438, sign: true });
a.append(FP16x16 { mag: 9580, sign: false });
a.append(FP16x16 { mag: 13240, sign: false });
a.append(FP16x16 { mag: 6426, sign: true });
a.append(FP16x16 { mag: 23823, sign: false });
a.append(FP16x16 { mag: 20440, sign: true });
a.append(FP16x16 { mag: 9714, sign: false });
a.append(FP16x16 { mag: 9210, sign: false });
a.append(FP16x16 { mag: 11646, sign: true });
a.append(FP16x16 { mag: 16809, sign: true });
a.append(FP16x16 { mag: 10461, sign: true });
a.append(FP16x16 { mag: 13050, sign: false });
a.append(FP16x16 { mag: 24717, sign: true });
a.append(FP16x16 { mag: 20103, sign: false });
a.append(FP16x16 { mag: 4465, sign: true });
a.append(FP16x16 { mag: 3913, sign: true });
a.append(FP16x16 { mag: 2117, sign: false });
a.append(FP16x16 { mag: 14813, sign: false });
a.append(FP16x16 { mag: 3847, sign: false });
a.append(FP16x16 { mag: 6198, sign: true });
a.append(FP16x16 { mag: 21279, sign: true });
a.append(FP16x16 { mag: 22213, sign: true });
a.append(FP16x16 { mag: 16859, sign: false });
a.append(FP16x16 { mag: 2136, sign: false });
a.append(FP16x16 { mag: 8308, sign: false });
a.append(FP16x16 { mag: 12437, sign: false });
}