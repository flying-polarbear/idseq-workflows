version 1.0
import "host_filter.wdl" as stage1
import "non_host_alignment.wdl" as stage2
import "postprocess.wdl" as stage3

workflow idseq_short_read_mngs {
    input {
        String docker_image_id
        File non_host_rapsearch2_index
        File non_host_gsnap_index
        String non_host_gsnap_genome_name = "nt_k16"
        String s3_wd_uri = ""
    }
    call stage1.idseq_host_filter as host_filter {
        input:
        docker_image_id = docker_image_id,
        s3_wd_uri = s3_wd_uri
    }
    call stage2.idseq_non_host_alignment as non_host_alignment {
        input:
        host_filter_out_gsnap_filter_1_fa = host_filter.gsnap_filter_out_gsnap_filter_1_fa,
        host_filter_out_gsnap_filter_2_fa = host_filter.gsnap_filter_out_gsnap_filter_2_fa,
        host_filter_out_gsnap_filter_merged_fa = host_filter.gsnap_filter_out_gsnap_filter_merged_fa,
        cdhitdup_cluster_sizes_cdhitdup_cluster_sizes_tsv = host_filter.cdhitdup_out_cdhitdup_cluster_sizes_tsv,
        cdhitdup_out_dedup1_fa_clstr = host_filter.cdhitdup_out_dedup1_fa_clstr,
        cdhitdup_out_dedup1_fa = host_filter.cdhitdup_out_dedup1_fa,
        local_gsnap_index = non_host_gsnap_index,
        local_gsnap_genome_name = non_host_gsnap_genome_name,
        local_rapsearch2_index = non_host_rapsearch2_index,
        docker_image_id = docker_image_id,
        s3_wd_uri = s3_wd_uri
    }
    call stage3.idseq_postprocess as postprocess {
        input:
        host_filter_out_gsnap_filter_1_fa = host_filter.gsnap_filter_out_gsnap_filter_1_fa,
        host_filter_out_gsnap_filter_2_fa = host_filter.gsnap_filter_out_gsnap_filter_2_fa,
        host_filter_out_gsnap_filter_merged_fa = host_filter.gsnap_filter_out_gsnap_filter_merged_fa,
        cdhitdup_cluster_sizes_cdhitdup_cluster_sizes_tsv = host_filter.cdhitdup_out_cdhitdup_cluster_sizes_tsv,
        cdhitdup_out_dedup1_fa_clstr = host_filter.cdhitdup_out_dedup1_fa_clstr,
        cdhitdup_out_dedup1_fa = host_filter.cdhitdup_out_dedup1_fa,
        gsnap_out_gsnap_m8 = non_host_alignment.gsnap_out_gsnap_m8,
        gsnap_out_gsnap_deduped_m8 = non_host_alignment.gsnap_out_gsnap_deduped_m8,
        gsnap_out_gsnap_hitsummary_tab = non_host_alignment.gsnap_out_gsnap_hitsummary_tab,
        gsnap_out_gsnap_counts_with_dcr_json = non_host_alignment.gsnap_out_gsnap_counts_with_dcr_json,
        rapsearch2_out_rapsearch2_m8 = non_host_alignment.rapsearch2_out_rapsearch2_m8,
        rapsearch2_out_rapsearch2_deduped_m8 = non_host_alignment.rapsearch2_out_rapsearch2_deduped_m8,
        rapsearch2_out_rapsearch2_hitsummary_tab = non_host_alignment.rapsearch2_out_rapsearch2_hitsummary_tab,
        rapsearch2_out_rapsearch2_counts_with_dcr_json = non_host_alignment.rapsearch2_out_rapsearch2_counts_with_dcr_json,
        docker_image_id = docker_image_id,
        s3_wd_uri = s3_wd_uri
    }
}