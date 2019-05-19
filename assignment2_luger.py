#! /usr/bin/env python3

import vcf

__author__ = 'Martina Marina Maria Luger'


class Assignment_2:

    def __init__(self, chr_22_file_name="chr22_new.vcf"):
        self.filename = chr_22_file_name
        ## Check if pyvcf is installed
        print("PyVCF version: %s" % vcf.VERSION)
        # Create reader object
        self.total_num_var = self.get_total_number_of_variants_of_file()

    def get_total_number_of_variants_of_file(self):
        '''
        Get the total number of variants
        :return: total number of variants
        '''

        variant_numb_total = 0 #counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                variant_numb_total += 1
        print("Total number of variants is ", variant_numb_total)
        return variant_numb_total
    ##output: 67784

    def get_average_quality_of_file(self):
        '''
        Get the average PHRED quality of all variants
        :return:
        '''

        sum_quality = 0
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                sum_quality = sum_quality + record.QUAL
        print("Average PHRED quality of the variants is: ", round((sum_quality / self.total_num_var), 2))
        return sum_quality
    ##output: 5.07

    def get_variant_caller_of_vcf(self):
        '''
        Return the variant caller name
        :return:
        '''

        variant_call = []
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                variant_call = record.INFO['callsetnames']
        print("The variant caller of vcf is ", variant_call[1])
    ##output: HiSeqPE300xfreebayes


    def get_human_reference_version(self):
        '''
        Return the genome reference version
        :return:
        '''

        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                info = record.INFO["difficultregion"]
                reference_v = info[0]
                print("The reference genome version is ", reference_v[0:4])
                break
    ##Output: hg38

    def get_number_of_indels(self):
        '''
        Return the number of identified INDELs
        :return:
        '''

        indel_numb = 0 #indel counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                if record.is_indel:
                    indel_numb += 1

        print("The number of indels is ", indel_numb)
        return indel_numb
    ##Ouput: 12774

    def get_number_of_snvs(self):
        '''
        Return the number of SNVs
        :return:
        '''

        num_snv = 0 #snv counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                if record.is_snp:
                    num_snv += 1
        print("The number of SNVs is ", num_snv)
        return num_snv
    ##Ouput: 55010


    def get_number_of_heterozygous_variants(self):
        '''
        Return the number of heterozygous variants
        :return:
        '''

        hetero_number = 0 #counter
        with open("chr22_new.vcf") as myVCF:
            vcf_reader = vcf.Reader(myVCF)
            for record in vcf_reader:
                hetero_number += record.num_het

        print("The number of heterozygous variants is ", hetero_number)
    #Output: 56370

    def merge_chrs_into_one_vcf(self):
        '''
        Creates one VCF containing all variants of chr21 and chr22
        :return:
        '''
        file = open("chr21_new.vcf")
        w_f = open("chr21_22_merged.vcf", "w+")
        for line in file:
            w_f.write(line)
        file.close
        w_f.close

        file = open("chr22_new.vcf")
        w_f = open("chr21_22_merged.vcf", "a")
        for line in file:
            w_f.write(line)
        file.close
        w_f.close

        print("Merged File with chr21 and chr22 was created.")

    def print_summary(self):
        self.get_average_quality_of_file()
        self.get_total_number_of_variants_of_file()
        self.get_variant_caller_of_vcf()
        self.get_human_reference_version()
        self.get_number_of_indels()
        self.get_number_of_snvs()
        self.get_number_of_heterozygous_variants()
        self.merge_chrs_into_one_vcf()

def main():
    print("Assignment 2")
    assignment2 = Assignment_2()
    assignment2.print_summary()
    print("Done with Assignment 2 :)")


if __name__ == '__main__':
    main()

