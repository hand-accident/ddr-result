<script>
    import GridCols1sm2md4 from "$c/GridCols1sm2md4.svelte";
    import YScrollContainerGradientTopN300 from "$c/YScrollContainerGradientTopN300.svelte";
</script>

<YScrollContainerGradientTopN300 class="l0">
    <GridCols1sm2md4 class="l1">
        <slot />
    </GridCols1sm2md4>
</YScrollContainerGradientTopN300>

<style lang="postcss" module>
    .l0 {
        @apply h-full mx-auto;
    }
    .l1 {
        @apply gap-4 p-4;
    }
</style>
