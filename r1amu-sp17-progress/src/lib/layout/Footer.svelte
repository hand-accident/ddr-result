<script>
    import FooterNeutral from "$c/FooterNeutral.svelte";
    import Rows from "$c/Rows.svelte";
</script>

<FooterNeutral class="l0">
    <Rows class="l1">
        <slot name="bio" />
    </Rows>
    <Rows class="l2">
        <slot name="links" />
    </Rows>
</FooterNeutral>

<style lang="postcss" module>
    .l0 {
        @apply justify-between px-4 py-2;
    }
    .l1 {
        @apply items-center;
    }
    .l2 {
        @apply gap-4;
    }
    @media (min-width: 768px) {
        .l2 {
            @apply place-self-center justify-self-end;
        }
    }
</style>
